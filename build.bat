if "%VCINSTALLDIR%"=="" call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall" x64
cl /O2 memtest.c
