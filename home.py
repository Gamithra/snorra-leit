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
                    <input id="search-form" name="keyword" placeholder="Leita úr Gylfaginningu"> </input>
                    <input type="image" id="search-icon" src="https://cdn1.iconfinder.com/data/icons/hawcons/32/698627-icon-111-search-512.png">
                </div>
                <p id="author"> <a href=https://github.com/Gamithra/snorra-leitarv-l>Kóðinn</a>: Gamithra Marga</p>
            </form>
    </div>

    <div id="container">
        % if greet:
            Leitarvélin sækir sjálfkrafa allar beygingarmyndir leitarorðsins frá <a>bin.is</a>.
        % else:
            <div id="result">
                % if success:
                    Leitarorð <i>"{{keyword}}"</i> fannst í eftirfarandi köflum:
                % else:
                    Leitarorð <i>"{{keyword}}"</i> fannst ekki!
                % end
            </div>
            % for chapter in search_results:
                <h1> {{chapter[0]}} </h1>

                % for paragraph in chapter[1]:
                    <p>
                    % for word in paragraph.split(" "):
                        % found = False
                        % for w in words:
                            % if w.lower() in word.lower():
                                % found = True
                                <b> {{word}} </b>
                                % break
                            % end
                        % end
                        % if not found:
                            % found = False
                            {{word}}

                        % end
                    % end
                    </p>
                % end
            % end

        % end

    </div>

</body>


</html>'''

def temp():
    return tpl


