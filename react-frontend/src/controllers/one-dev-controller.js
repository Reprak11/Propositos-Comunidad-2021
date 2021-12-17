export const OneDevsController = (name) =>{
    return fetch('http://localhost:5000/api/v1/0/onegoal/',{
        method:"GET",
        headers:{
            "Content-Type":"application/json",
            "name":name
        }
    })
    .then((response) =>{
        return response.json()
    })
    .then((data)=>{
        return data
    })
}