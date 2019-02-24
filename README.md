# Shazam 4 Petz!

Live Website: [https://shazam4petz.github.io/](https://shazam4petz.github.io/)


## Our Mission

Create a high-accuracy tool for shelters to **correctly identify breed combinations and percentages** of cross and mixed-bred dogs and cats using `machine learning`, and help **raise adoption rates** of shelter animals as a result.


## The Problem

According to an article in the [Smithsonian](https://www.smithsonianmag.com/smart-news/genetic-testing-shows-animal-shelters-often-misidentify-dogs-breeds-180970136/) (2018), roughly 3.3 million dogs enter animal shelters in the U.S. each year, but only an alarming **67%** are correctly identified of their primary or secondary breed by shelter staffs. Leaving **over 1.089 million dogs** across the country to be **misidentified or mislabeled** yearly.

Currently, there are no standardized procedures across the U.S. for identifying breeds of dogs and cats. The accuracy rate for breed-identification varies significantly from shelter to shelter and staff to staff. [Studies show that](https://www.vetmed.ufl.edu/2016/02/17/dna-studies-reveal-that-shelter-workers-often-mislabel-dogs-as-pit-bulls/) as high as **48%** of dogs with no genetic evidence of being Pit Bulls have been misidentified as Pit Bull-type dogs. Widely *(and incorrectly)* believed to be "dangerous" and aggressive in nature, **Pit Bulls** have one of the **lowest adoption rates**, and maintains to be **the most commonly restricted dog breed** from "pet-friendly" rental properties.

Inaccurate breed-labelling of shelter animals **drastically limits their pool of potential adopters**, and as a result, **directly lowers their chances of being adopted.**

<!--

Inaccurate breed-identification drastically reduces the pool of potential adopters as **Pit Bulls** are the **most commonly restricted dog breed** of many "pet-friendly" rental properties, leading to *much* **lower rates of adoption** for mislabeled dogs.

In the dogs that are mislabeled, [many](https://www.vetmed.ufl.edu/2016/02/17/dna-studies-reveal-that-shelter-workers-often-mislabel-dogs-as-pit-bulls/) are be labeled as **Pit Bulls**, a **commonly restricted dog breed** for many rental properties. This deadly mix-up costs <u>**limits their pool of potential adopters**</u>, and <u>**dramatically lowers their chances of being adopted**</u>.

Aside from the issue of breed-specific bans on pets (also hugely problematic), mislabeling dogs as unfavorable breeds directly **strips them of possibilities to be adopted**.

Sadly, this is not something we can reverse within a weekend. However, we *can* start by building a user-friendly tool that accurately <u>identifies possible breed combinations and percentages using a custom-trained Machine Learning Model.</u>

-->


<!--
## Our Results


-->


## Our Awards

| :trophy: [Best Use of Google Cloud Platform](https://twitter.com/MLHacks/status/1094702441151545344) | :trophy: Best Almost Hack |
| :---: | :---: |
| <img src="https://github.com/shazam4petz/shazam4petz.github.io/blob/master/img/Award_GCP.gif"/> | <img src="https://github.com/shazam4petz/shazam4petz.github.io/blob/master/img/Award_Almost.gif"/> |


## Tech Stacks

* [Firebase](https://firebase.google.com/): Cloud Storage, Realtime Database, User Authentication
* [Google Cloud Vision API](https://cloud.google.com/vision/): Image Analysis
* [Google Cloud AutoML Vision](https://cloud.google.com/vision/automl/docs/): Custom Machine Learning Model Training
* [Google Cloud Functions](https://cloud.google.com/functions/): Serverless Application Scripts
* [Google Colab](https://colab.research.google.com/): Collaborative Python IDE


## Future Development

* Further train our Model with more data, improving its precision as it scales
* Implement a validation/filtering algorithm for photos uploaded by users
* Store approved photos uploaded by users to our database for further Model-training
* iOS & Android Apps: allowing photos taken via mobile phones to be analyzed direct within our app
* Using the Wolfram Alpha API, provide users with health information for specific mix-breeds of dogs and cats
* Expand our coverage to other species of animals


## Our Team

Brought together by our mutual love for animals, we found each other at the team-forming workshop of [Hack(H)er413](https://www.hackher413.com/), a 2-day hackathon from Feb 09-10, 2019, on the  [UMass Amherst](https://www.umass.edu/) campus.

* [Miffy Chen](https://miffychen.tech/): Website, Google Cloud Platform, Design, Integration
* [Anna Mun](https://shazam4petz.github.io/aboutus/index.html): Cloud Vision API
* [Qing Zhao](https://shazam4petz.github.io/aboutus/index.html): AutoML Model
* [Stephanie Murphy](https://shazam4petz.github.io/aboutus/index.html): REST API
