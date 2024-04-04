mkdir bitcoin_smart_assistant
cd bitcoin_smart_assistant
python3 -m venv venv
source venv/bin/activate
pip install requests  # We'll use requests to call APIs
echo "venv/" > .gitignore
git init
