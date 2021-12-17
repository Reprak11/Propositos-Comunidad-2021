import React,{useState ,useEffect} from 'react'
import OneGoalInfo from '../components/OneGoalInfo'
import ListGoals from '../components/ListGoals'
import { OneDevsController } from '../controllers/one-dev-controller'


const Goals = () => {
    const [oneData, setOneData] = useState([])

    useEffect(() => {
        async function fetchData(){
        await OneDevsController("Reprak").then(data => {
            setOneData(data)
        })
    } fetchData();}, []);

    async function changeName(name){
        await OneDevsController(name).then(data => {
            setOneData(data)
        })
    } 
    
    console.log(oneData)
    return(
        <div className="goals">
            <OneGoalInfo oneData={oneData} />
            <ListGoals changeName={changeName} />
        </div>
)}

export default Goals