import { useState, useEffect, useRef } from "react";
import ReactDOM from "react-dom/client";

function App() {
    const [inputValue, setInputValue] = useState("");
    const previousInputValue = useRef("");

    useEffect(() => {
        previousInputValue.current = inputValue;
    }, [inputValue]);
    var todoList = [];
    let number = 0;
    function sayImput() {
        console.log(inputValue);
        todoList = [{ name: inputValue, id = number }, ...todoList];
        number++;
        console.log(todoList);
    }
    return (
        <>
            <div id="input">
                <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                />
                <button onClick={sayImput}>Add Todo</button>
            </div>
        </>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
