title: Review : Two Practical Books on Visualizations
subtitle: Visualization book by the author of FlowingData.com
date: 2016-06-06 21:52
tags: books, D3, visualization
cover_image: /images/bookcover/visualize_this_data_points.jpg
D3:
scripts: d3_pie_chart.js
styles: d3_pie_chart.css

Two excellent books that can help you get started with effective visualization of your data are: The [**Data Points**: Visualization that means something](https://www.amazon.com/gp/product/111846219X) and [**Visualize This**: The FlowingData Guide to Design, Visualization, and Statistics](https://www.amazon.com/gp/product/0470944889). These best seller are written by **Nathan Yau** who is also the author of the famous data visualization blog:  [FlowingData](http://flowingdata.com/). 

*Data Points* explains the core principles of visualization and inspires its reader about the effective use of this medium to tell a story about their data. It walks you through the best representation of different types of data and how they compare with each other. The book itself comes with a lot of inspiring examples that are beautifully crafted and are visually pleasing. Once you are ready to dive deep and get your own hand dirty with the material, you can head over to the *Visualize This* and get a more technical introduction of the topic. 

*Visualize This* offers a more hands on approach to visualizing data. It offers concrete step-by-step guide for creating different types of visualization using R, Python and Javascript. You also learn about the process of enhancing and annotating your plot using a tool like Adobe Illustrator. The end result is a refined and pleasing illustration that tells a good story. These books are no where a complete guide on this topic but it can offer a solid start. 

To conclude, take a look at few of the examples from the books. These are primarily based on the code given in the *Visualize This*. However, for the third example, instead of making the pie chart in [Protovis](http://mbostock.github.io/protovis/) as explained in the book, I used [D3](https://d3js.org/). Protovis is no longer in active development and it seems D3.js completely replace it. 

### Example # 1: Bar Chart

A bar chart for showing the number of hot dog buns eaten by each year contestents.

![post](/images/visualize-this-nathan-yau/hotdogcontest_ai.png)

### Example 2: Plotting data on Map

A map plot showing unemployment rate during August of 2010 across the United States. 

![post](/images/visualize-this-nathan-yau/unemployment.png)

### Example 3: Pie Chart

A simple bar chart made using D3.js. You can look at the source code for this example [here](https://gist.github.com/n-log-n/7b2573a52072aae8da1fb7569bcb4ce7)

<div class="d3-chart"></div>
