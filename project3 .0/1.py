with open(r'C:\Users\24113\ldproject\project3 .0\result\1.bat','w') as f:
    f.write("""@echo off
echo open testreport
allure open .\html
pause
    """)