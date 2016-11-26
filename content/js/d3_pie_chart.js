var data  = [
                {"cat": "Statistics", "count" : 172},
                {"cat" : "Design", "count" : 136},
                {"cat" : "Business", "count" : 135},
                {"cat" : "Cartography", "count" : 101},
                {"cat" : "Information Science", "count" :  80},
                {"cat" : "Web Analytics", "count" : 68},
                {"cat" : "Programming", "count" : 50},
                {"cat" : "Engineering", "count" : 29},
                {"cat" : "Mathematics", "count" :  19},
                {"cat" : "Other", "count" : 41}
            ];

var width = 750,
    height = 500,
    radius = Math.min(width, height) / 2;

var color = d3.scale.linear().domain([0, 172]).range(["white", "#821122"]);

var arc = d3.svg.arc()
            .outerRadius(radius)
            .innerRadius(radius * .25)
            .padAngle(.01);

var pie = d3.layout.pie()
            .sort(null)
            .value(function(d) { return d.count; });

var svg = d3.select(".d3-chart").append("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

var g = svg.selectAll(".arc")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc");

        g.append("path")
            .attr("class", "darc")
            .attr("id", function(d, i) { return "darc_" + i; })
            .attr("d", arc)
            .style("fill", function(d) { return color(d.data.count); });

        g.append("text")
            .attr("transform", function(d) { 
                var angle = (d.startAngle + d.endAngle) * 90/Math.PI - 90;
                angle = angle > 90 ? angle - 180 : angle;

                return "translate(" + arc.centroid(d) + ") rotate(" + angle + ")" ;}
             )
            .attr("dy", ".35em")
            .style("text-anchor", "middle")
            .style("fill", "White")
            .text(function(d) { return d.data.cat; });
