# FullStackProject

Introduction (20 points)
Domain and Motivation
Our project delves into the domain of personal finance, focusing on a pressing issue
many consumers face today: credit card debt consolidation and balance transfers. The motivation
behind this project stems from the complexities and challenges consumers encounter when
navigating the myriad of options available for managing and consolidating credit card debts. This
endeavor aims to streamline this procedure, transforming it to be more transparent and
user-friendly, regardless of their level of financial expertise.

Terminology/Jargon
Firebase - is a popular development platform offered by Google and is widely used in
building mobile and web applications.
CSS - Cascading style sheets are the cornerstone technology of the web, alongside
HTML and JavaScript. It is used for the styling and layout of web pages.
Javascript is a powerful and versatile programming language widely used in web
development.
SQLite3 - a lightweight, usually embedded database that does not require a separate
server process.
Machine Learning is a branch of artificial intelligence that focuses on building systems
that are capable of learning and making decisions given different kinds of data.
Random Forest - Machine learning algorithm that is used for classification and
regression.
Django - is an open-sourced web framework written in Python, designed to facilitate the
rapid development of web applications.

History

Historically, the implementation of debt consolidation and balance transfer has always
been a lengthy procedure, copious amounts of documentation, and requires manual evaluation of
financial instruments. On the contrary, although these procedures have been significantly
optimized since the inception of financial technology, a noticeable gap persists regarding the
availability of a cohesive platform that streamlines comparisons and facilitates decision-making
regarding individual financial profiles.

Objectives

Our project's primary objective revolves around developing a user-friendly web
application to streamline the comparison of debt consolidation and balance transfer options
across various credit cards. Our overarching goals include providing consumers a platform to
evaluate credit card choices tailored to their individual profiles and financial objectives.
Specifically, we aim to implement a Django front-end landing page, integrate percentages for a
machine learning algorithm to analyze credit card options, and develop a web form to collect
user data. We've successfully addressed challenges related to the Django project's logic, machine
learning algorithm implementation, and web form integration.

However, obstacles arose in obtaining accurate data from credit card companies through
APIs, leading us to pivot our strategy. Our revised plan involves using sample data from other
websites for testing, focusing on algorithm training and validation to reduce external
dependencies. The success of our project hinges on overcoming risks associated with ensuring
accurate database collection of user data, managing project timelines amidst other class
commitments, comprehending Django back-end programming intricacies, and presenting the
project effectively.

Our project aligns with the current state of financial technology by addressing dynamic
challenges in credit card decision-making. Our web application stands out in the era of
personalized and data-driven solutions, providing users with a sophisticated tool to compare debt
consolidation and balance transfer options based on their unique financial profiles. Integrating a
machine learning algorithm reflects a forward-looking approach, leveraging cutting-edge
technologies. Our adaptation to using sample data for testing demonstrates a pragmatic response
to challenges, contributing to the ongoing evolution of financial technology.

Methodology

Machine Learning Model
A 4000-row dataset of loan and credit card application data was obtained from Kaggle to
train a machine learning model to evaluate the likelihood of loan repayment. The Sklearn Python
library was used to import the dataset and split the data into training and evaluation datasets.
After the data was split, a Random Forest Regression model was created. The loan status
was mutated into binary values of 1 and 0, indicating loan repayment and default, respectively.
Loan status was set as the dependent variable, and other indicators, such as assets, income, FICO
score, etc., were selected as the independent variables. A Random Forest of 10,000 trees was
created and then fit with a mean absolute error of 0.08. With the model fit, predictions could then
be made. The model produces a score of between 0 and 1. A score of 0.50 or greater is required
for approval, and others are denied. This model proves efficacy providing efficient and accurate
loan decision-making.

Results (25 points)
Achievements and Quantitative Results

The development of our web application for credit card debt consolidation and balance
transfer has achieved several significant milestones. We have successfully implemented a
user-friendly interface, making it accessible and intuitive for users of varying levels of
tech-savviness. This interface provides a seamless experience, from account registration to
viewing and managing debt balances.

One of the project's significant accomplishments is integrating a machine learning
algorithm, utilizing users' debt ratios and credit scores to identify and recommend the most
beneficial balance transfer options. This feature not only enhances the user experience but also
adds a layer of personalization, tailoring recommendations to individual financial situations.
Additionally, we included the integration of educational resources on personal finance
management to enhance the application's value proposition, which also aligns with our goal of
making financial management more accessible to a broader audience.

Finally, we were able to utilize many web tools in our program. Using Django, we used
HTML, CSS, JavaScript, and Python to create a functional and visually pleasing platform.
Django’s SQLite3 database was used to store the user's responses and pulled from the Python
machine learning code. The last tool we implemented was the Firebase authentication for signing
into the application. We can pull the user’s name from the login information for a customized
dashboard.

Learning Outcomes and Challenges
Throughout the project, our team has encountered various challenges and learning
opportunities. One significant challenge was the pivot from using APIs from credit card
companies to employing sample data for testing and algorithm training. This decision, though
necessary, required us to adapt our approach to data acquisition and integration.
Our team also navigated through the complexities of Django for both front-end and
back-end development. Understanding and effectively utilizing this framework was crucial for
integrating different components of our application, especially in ensuring seamless navigation
and user data management. Another learning aspect was balancing project management with
technical development. This involved aligning project deadlines with class requirements and
managing the learning curve associated with new technologies and programming languages.

Conclusion (30 points)

Summary of Findings
Our project has successfully demonstrated fintech's potential in revolutionizing how
consumers manage credit card debt. Our team's web application achieves its intended
functionality and adds value through its user-centric design and innovative features. Ultimately,
it effectively bridges the gap in the market for a unified platform that simplifies the process of
credit card debt consolidation and balance transfers.
The core functionalities of our application, including the machine learning algorithm
utilized to generate personalized recommendations, the capability to link and access credit card
data, and the capability to commence and monitor balance transfers, have proven to be incredibly
influential. These features give users a new level of control and insight into improving their
financial health.

Insight/Reflection
Our team has acquired invaluable insights into the convergence of finance and
technology over the course of this project. Having a better understanding of the criticality of user
experience design when developing financial applications, especially the importance of
functional, intuitive, and accessible applications that accommodate users with diverse financial
expertise. Furthermore, this project demonstrated how critical it is for adaptability and resiliency
when it comes to project management. Our team quickly pivoted from the planned infrastructure
in light of external constraints, as demonstrated by our transition from utilizing external APIs to
employing sample data for development.

Future Developments
In the future, there are several avenues for further development and expansion of the
project. Our immediate goal is to release the minimum viable product (MVP) and obtain user
feedback to improve the application’s features and user-friendliness. Recognizing the increasing
use of mobile applications, we also intend to develop a mobile version of our platform, to
accommodate the convenience of financial management on the go. Next would be incorporating
more diverse financial products, such as loans and mortgages, which could broaden the
application's scope and utility. Additionally, advanced machine learning algorithms could be
implemented for more nuanced financial recommendations, considering factors like spending
habits and financial goals. The successful implementations of APIs can also help users to
seamlessly and securely connect to their accounts, as well as exploring the possibility of
introducing an innovative feature that enables users to directly close or consolidate cards within
the application. The integration of this feature will revolutionize the process of managing debt by
providing users with an enhanced convenience in optimizing their credit card accounts.
In conclusion, this project has achieved its immediate objectives and paved the way for
further exploration in personal finance and fintech, demonstrating our team's ability to overcome
challenges and adapt to changing circumstances.
