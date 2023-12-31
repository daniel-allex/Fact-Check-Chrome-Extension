# Fact-Check-Chrome-Extension
A google chrome extension that:
* Marks up misinformation on websites
* Gives political leanings of websites
* Tells the user political leanings of journalists and other mentioned political figures

The server uses Approximate Nearest Neighbors (ANN) vector searches to find the embedding vectors for scraped sentences from Politifact that are similar to embedding vectors for sentences from a given web page. It loads in from MongoDB at first from the automatic scraping to update a persistent vector space for ANN. The solution dereferences nouns so that indirect nouns such as pronouns become the corresponding exact noun to improve accuracy.

# To Run
1. If you are on windows- go to https://visualstudio.microsoft.com/visual-cpp-build-tools/ and select the C++ build tools. Ensure the "Windows SDK" for your Windows versions and the latest "MSVCv142 - VS 2019 C++ x64/x86 build tools" are selected
2. Enter the install commands specified in Dependencies.txt in terminal
3. In Google Chrome, go to the Extensions page from the 3 dots at the top right corner
4. Turn on "Developer Mode" at the top right corner
5. Click "Load unpacked" in the top left corner
6. Select the "extension" folder in the main directory
