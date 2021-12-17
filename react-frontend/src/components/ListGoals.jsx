import React, {useState ,useEffect} from 'react'
import { AllDevsController } from '../controllers/all-devs-controllers'

const ListGoals = ({changeName}) => {
    const [myData, setMyData] = useState([])

    useEffect(() => {
        async function fetchData(){
        await AllDevsController().then(data => {
            setMyData(data)
        })
    } fetchData();}, []);
    
    return(
    <div className="list-goals">
        <ul className="user-list">
            {(myData.map(names => <li key={names["name"]} onClick={() => changeName(names["name"])} className="one-user"><p className="user-list-name">{names["name"]}</p></li>))}
        </ul>
        
    </div>
)
}
export default ListGoals