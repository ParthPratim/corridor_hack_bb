import { React, useState }from "react";
import axios from "axios";
import './Form.css'
import image from "./assets/image.jpeg"
const submitHandler =(event) => {
    event.preventDefault();
    var doc_request = {
        "section_1" : {
            "devname" : event.target[0].value,
            "modelname"  : event.target[1].value,
            "overview": event.target[2].value
        },
        "section_2": {
            "content" : event.target[3].value,
        }
    }

    // console.log(event.target[1].value)

    var json_str = JSON.stringify(doc_request)
    doc_request = json_str
    // const file = event.target[4].value;
    const data = new FormData()
    data.append("doc_request",doc_request)
    data.append("file",event.target[4]);
    axios.post("http://127.0.0.1:6969/api/doctool/generate/",data)
}
const Form = () => {
    const[devname, setDevname] = useState("");
    const[modelname, setModelname] = useState("");
    const[modeloverview, setModeloverview] = useState("");
    const[modelselection, setModelselection] = useState("");
    const[file, setFile] = useState("");


    return (
        <div className="container-full">
        <div style={{display:'flex'}}>
        <div className="column-right">
            <img src={image} width={700} height={700} alt="vector"/>
        </div>
            <form className="login-form" method="post" action="http://127.0.0.1:6969/api/doctool/generate/" enctype="multipart/form-data" >
            <h1>Generate your ML Document!</h1>
                <div className="form-input-material">
                    <label htmlFor='devname'>Developer Name : </label>
                    <input type= "text" name = "devname" id="devname" autoComplete="off" className="form-control-material"
                    value={devname}
                    onChange ={(e) => setDevname(e.target?.value)}
                    />
                </div>
                <div className="form-input-material">
                    <label htmlFor='modelname'>Model Name : </label>
                    <input type= "text" name = "modelname" id="modelname" autoComplete="off" className="form-control-material"
                    value={modelname}
                    onChange ={(e) => setModelname(e.target?.value)}
                    />
                </div>
                <div className="form-input-material">
                    <label htmlFor='modeloverview'> Model Overview : </label>
                    <textarea rows={5} cols={15}  name ="overview" autoComplete="off" className="form-control-material"
                    value={modeloverview} 
                    onChange ={(e) => setModeloverview(e.target?.value)}
                    />
                </div>
                <div className="form-input-material">
                    <label htmlFor='modelselection'>Reason for Model Selection : </label>
                    <textarea rows={5} cols={15} name = "content" id="modelselection" autoComplete="off" className="form-control-material"
                    value={modelselection}
                    onChange ={(e) => setModelselection(e.target?.value)}
                    />
                </div>
                <div className="form-input-material">
                <label htmlFor='file'>File : </label>
                <input type= "file" name = "file" id="file"
                value={file} 
                onChange={(e) => setFile(e.target?.value)}    
                />
                </div>
                <button type='submit' className="btn btn-primary btn-ghost">Generate PDF</button>
            </form>

        </div>
        </div>
    )
}

export default Form;
