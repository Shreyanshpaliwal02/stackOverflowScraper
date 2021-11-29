# stackOverflowScraper
Description: This is simple Python and HTML requests project to search StackOverflow.com for a large number of queries at once.

Utility: Using this project, the user can get thousands of results in few minutes automatically. The scrape results i.e., the questions(for eg: "How do JavaScript closures work?") related to a particular tag(Eg- "Python", "C++", "Machine Learning" etc) can be answered by the user for enhancing the knowledge of the subjects. 

RESULT:
![image](https://user-images.githubusercontent.com/92806875/143820854-8ba428f1-1420-4e7c-b0f8-512238a93d4f.png)

Selecting the base Url to be scraped:
![image](https://user-images.githubusercontent.com/92806875/143813895-f84b778b-04d3-4b05-9e9d-8f519c8d1127.png)

How to search the tags associated with a particular query in the base URL:
  1. Inspect Element for the question, votes, and hashtags. For eg: 
  ![image](https://user-images.githubusercontent.com/92806875/143816236-834af060-4e7b-4d3c-8e91-31ac32dde177.png)
  2. Each selected element has its own class in HTML. For the question, the class is '.question-hyperlink', hence we add this in the classesRequired list in the code.
  ![image](https://user-images.githubusercontent.com/92806875/143816487-7817b79c-f738-4ba3-b355-b2ba5a6944e0.png)

Finding the required Query on the base URL and associated tags on python:
![image](https://user-images.githubusercontent.com/92806875/143814010-bf912105-e6a3-4b78-a53b-a7b3377da7e3.png)

Above output contains the following elements from the base URL:
" columns = ['votes', 'vote_title', 'num_answers', 'views', 'question', 'description', 'tags', 'date', 'user', 'user_details'] "

Filtering to collect only required entries and creating a template function for the desired output: 
![image](https://user-images.githubusercontent.com/92806875/143814384-7bbbbf1c-b636-4d0d-8e08-9d112706fc1d.png)

Uploading the CSV output into Pandas Dataframe and printing the first five elements(The data is uploaded into an Excel sheet)
![image](https://user-images.githubusercontent.com/92806875/143815277-11c78002-7475-43e7-a132-bb6c768c5c5d.png)

Dependencies:
requests,
HTML,
pandas
Environment: Jupyter Notebook

Tutorial Can be found here: "https://www.youtube.com/playlist?list=PLEsfXFp6DpzQjDBvhNy5YbaBx9j-ZsUe6"
