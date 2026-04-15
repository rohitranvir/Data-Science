    import React, { useEffect } from 'react'


    const Child = ({clickfn})=> {
        useEffect(()=>console.log("hii..."))
    return (
        <button onClick={clickfn}>
            Child Button
        </button>
    )
    }

    export default React.memo(Child)
