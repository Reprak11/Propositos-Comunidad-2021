import React from 'react'



const OneGoalInfo = ({oneData}) => {
    

    return(
    <div className="one-goal">
        {oneData["name"] && <h1>{oneData["name"]}</h1>}
        {oneData["resume"] && <h1>{oneData["resume"]}</h1>}
        {oneData["goal_one"] && <h1>{oneData["goal_one"]}</h1>}
        {oneData["goal_two"] && <h1>{oneData["goal_two"]}</h1>}
        {oneData["goal_three"] && <h1>{oneData["goal_three"]}</h1>}
        {oneData["contact"] && <h1>{oneData["contact"]}</h1>}
    </div>
)
}

export default OneGoalInfo