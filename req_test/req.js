var request = require('request')

function queryString(arr) {
    var obj = new Array();
    for (var key in arr) {
        obj.push(key + '=' + encodeURIComponent(arr[key]));
    }
    return obj.join('&');
}

function makeRequest(method) {
    var data = {
        a: 1,
        b: 2,
        c: 3
    };

    var req = request({
        uri: 'http://localhost:3000/app',
        method: method,
        body: queryString(data),
        headers: { 'content-type': 'application/x-www-form-urlencoded' }
    }, function(err, data) {
        if (err) console.log(err)
        else console.log(data.body)
    })
};

makeRequest('GET');
makeRequest('PUT');
makeRequest('POST');
makeRequest('DELETE');