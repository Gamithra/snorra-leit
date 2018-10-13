tpl = '''
<html>

<head>
     <meta charset="utf-8">
     <title>Snorra-leit</title>
     <link rel="stylesheet" href="static/style.css">
</head>

<body>

    <div id="search">
        <!--div id="search-title">Leita úr Snorra-Eddu </div-->
            <form action="http://localhost:8080/" method="post">
                <div id="search-div">
                <input id="search-form" name="keyword" placeholder="Leita úr Snorra-Eddu"> </input>
                <input type="image" id="search-icon" src="https://cdn1.iconfinder.com/data/icons/hawcons/32/698627-icon-111-search-512.png">
                </div>
            </form>
    </div>

    <div id="container">
        {{search_results}}

    </div>

</body>


</html>'''

def temp():
    return tpl
