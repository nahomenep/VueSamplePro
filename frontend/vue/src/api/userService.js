export const getIndData = function() {
    return new Promise((resolve , reject) => {
        fetch("http://localhost/api/getIndData?userId=1", {
            method: 'GET',
            headers:{'content-type': 'application/json'},
            mode: 'no-cors'
        }).then((response) => {
            //console.log(response.status);
            console.log(response);
            resolve(response);
          }).catch(() => {
            console.log("error caught!");
          });
    })
}


export const getAllData = function() {
    return new Promise((resolve, reject) => {
        fetch("http://localhost/api/user", {
            method: 'POST',
            headers:{'content-type': 'application/json'},
            mode: 'no-cors'
        }).then((response) => {
            //console.log(response.status);
            console.log(response);
          }).catch(() => {
            console.log("error caught!");
          });
    });
}

export const saveStaff = function(staff) {
    return new Promise((resolve , reject) => {
        fetch("http://localhost/api/getIndData?userId=1", {
            method: 'GET',
            headers:{'content-type': 'application/json'},
            mode: 'no-cors'
        }).then(res=>res.json()
        ).then(data=>
            console.log(data)
        )
    });
}
