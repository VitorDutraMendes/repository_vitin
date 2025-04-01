#!/bin/bash
echo "configurando git..."
git config --global user.name "Vitormendes123"
git config --global user.email "vitordmendes110@gmail.com"

echo "configurando VsCode..."
code --install-extension 2gua.rainbow-brackets
code --install-extension bmewburn.vscode-intelephense-client
code --install-extension bradlc.vscode-tailwindcss
code --install-extension dbaeumer.vscode-eslint
code --install-extension dracula-theme.theme-dracula
code --install-extension eamodio.gitlens
code --install-extension ecmel.vscode-html-css
code --install-extension felixfbecker.php-intellisense
code --install-extension formulahendry.auto-close-tag
code --install-extension formulahendry.auto-rename-tag
code --install-extension gencer.html-slim-scss-css-class-completion
code --install-extension MS-CEINTL.vscode-language-pack-pt-BR
code --install-extension code --install-extension code --code --install-extension install-extension onecentlin.laravel-blade
code --install-extension onecentlin.laravel5-snippets
code --install-extension PKief.material-icon-theme
code --install-extension ritwickdey.LiveServer
code --install-extension TabNine.tabnine-vscode
code --install-extension vscode-icons-team.vscode-icons
code --install-extension xabikos.JavaScriptSnippets
code --install-extension Zignd.html-css-class-completion

echo "Não se esqueça de copiar a pasta '.vscode' para dentro da pasta do seu projeto!"
