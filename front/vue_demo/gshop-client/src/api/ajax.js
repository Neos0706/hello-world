import axios from "axios";

export default function ajax(url, data = {}, type = 'GET') {
    return new Promise(function(resolve, rejecct) {
        let promise
        if (type === 'GET') {
            //准备拼接字符串
            let dataStr = ''
            Object.keys(data).forEach(key => {
                dataStr += key + '=' + data[key] + '&'
            })
            if (dataStr !== '') {
                dataStr = dataStr.substring(0, dataStr.lastIndexOf('&'))
                url = url + '?' + dataStr
            }

            //发送get请求
            promise = axios.get(url)
        } else {
            //发送post请求
            promise = axios.post(url, data)
        }
        promise.then(response => {
            resolve(response.data)
        }).catch(error => {
            rejecct(error)
        })
    })

}