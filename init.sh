if !(type "brew" > /dev/null 2>&1); then
    echo "You need to install brew"
    exit 1;
fi
if !(type "fish" > /dev/null 2>&1); then
    brew install fish
fi
if !(type "python3.10" > /dev/null 2>&1); then
    brew install python@3.10
fi
rm -rf ./.venv
python3.10 -m venv .venv
if [ ! -d "images" ]; then
    mkdir images
fi
echo "
source .venv/bin/activate.fish
pip install -r requirements.txt
" | fish

echo "__________ DO THIS __________"
echo "fish"
echo "source .venv/bin/activate.fish"
echo "python ."
