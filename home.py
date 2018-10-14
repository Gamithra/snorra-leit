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
            <form action="http://localhost:8080/" method="post" accept-charset="ISO-8859-1">
                <div id="search-div">
                    <input id="search-form" name="keyword" placeholder="Leita úr Snorra-Eddu"> </input>
                    <input type="image" id="search-icon" src="https://cdn1.iconfinder.com/data/icons/hawcons/32/698627-icon-111-search-512.png">
                </div>
                <p id="author"> <a href=https://github.com/Gamithra/snorra-leitarv-l>Kóðinn</a>: Gamithra Marga</p>
            </form>
    </div>

    <div id="container">
        % for pr in search_results:
            <p>{{pr}}</p>
        % end

        % if greet:
            Leitarvélin sækir sjálfkrafa allar beygingarmyndir leitarorðsins frá <a>bin.is</a>.
        % end

    </div>

</body>


</html>'''

def temp():
    return tpl
