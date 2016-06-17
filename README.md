How to use (for odoo v8)

![alt tag](https://raw.githubusercontent.com/pquochoang2007/view_inbox_image/master/image_viewer/readme/result.png)


```javascript
    $http.jsonp('http://localhost:8888/widget/list?callback=JSON_CALLBACK', {
                params: {
                    index: 0,
                    limit: 10
                }
            }).then( // do something );
```
