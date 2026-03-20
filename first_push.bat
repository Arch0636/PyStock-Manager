@echo off

echo ===============================
echo Inicializando repositorio Git
echo ===============================

git init

echo.
echo Adicionando arquivos...
git add .

echo.
set /p msg=Digite a mensagem do primeiro commit: 

git commit -m "%msg%"

echo.
echo Conectando ao repositorio remoto...

git branch -M main

git remote add origin https://github.com/Arch0636/PyStock-Manager.git

echo.
echo Enviando arquivos para o GitHub...

git push -u origin main

echo.
echo Projeto enviado com sucesso!
pause