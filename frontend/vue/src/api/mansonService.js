export const getIndData = function(staff) {
    return new Promise((resolve , reject) => {
        fetch("http://localhost/api/getIndData?userId=1", {
            method: 'GET',
            headers:{'content-type': 'application/json'},
            mode: 'no-cors'
        }).then(
            res => resolve(res)
        )
    });
}

export const getAllData = function() {
    return new Promise((resolve, reject) => {
        fetch(`${process.env.VUE_APP_SERVER_URL}/staffs`, {
            method: 'GET'
        }).then(
            res => resolve(res)
        )
    });
}