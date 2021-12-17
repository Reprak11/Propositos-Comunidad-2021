export const AllDevsController = () =>{
    return fetch('http://localhost:5000/api/v1/0/goals/',{
        method:"GET"
    })
    .then((response) =>{
        return response.json()
    })
    .then((data)=>{
        return data
    })
}