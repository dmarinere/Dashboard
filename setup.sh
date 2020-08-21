mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"dmarinere@gmail.com\"\n\
" > ~/.streamlit/credentials.toml


echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[browser]
serverAddress = "https://dashboard-emma.herokuapp.com/" 
" > ~/.streamlit/config.toml
