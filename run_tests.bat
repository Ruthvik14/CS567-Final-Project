@echo off
setlocal enabledelayedexpansion

REM Define the original and backup filenames
set ORIGINAL_FILE=database.py
set BACKUP_FILE=database_backup.py

REM Variables for tracking test results
set /A KILLED_MUTANTS=0
set /A TOTAL_MUTANTS=0

REM Backup the original database.py file
echo Backing up the original database file...
copy /Y "%ORIGINAL_FILE%" "%BACKUP_FILE%"

echo Listing all mutant files in the directory:
dir /B *mutant*.py

echo Starting mutation testing...
echo.

REM Loop through each mutant file and run the unit tests
for %%f in (*mutant*.py) do (
    echo -------------------------------------------------------------------------------
    echo Testing mutant: %%f
    echo -------------------------------------------------------------------------------

    REM Replace the original file with the current mutant
    copy /Y "%%f" "%ORIGINAL_FILE%"

    REM Increment the total mutants counter
    set /A TOTAL_MUTANTS+=1

    REM Execute the Python unit tests
    echo Running tests for %%f...
    python -m unittest test
    if errorlevel 1 (
        echo TESTS FAILED FOR %%f - MUTANT KILLED
        set /A KILLED_MUTANTS+=1
    ) else (
        echo TESTS PASSED FOR %%f - MUTANT SURVIVED
    )

    echo.
    echo Press any key to continue to the next mutant...
    pause
)

REM Restore the original database file
echo Restoring the original database file...
copy /Y "%BACKUP_FILE%" "%ORIGINAL_FILE%"
del "%BACKUP_FILE%"

REM Calculate and display the mutation score
set /A MUTATION_SCORE=(KILLED_MUTANTS * 100) / TOTAL_MUTANTS
echo Mutation testing complete.
echo Total Mutants: %TOTAL_MUTANTS%
echo Killed Mutants: %KILLED_MUTANTS%
echo Mutation Score: %MUTATION_SCORE%%% 

endlocal
