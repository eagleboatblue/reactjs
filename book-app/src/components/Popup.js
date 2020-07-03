import React from "react";
import Popup from "reactjs-popup";
import AddBookForm from "./forms/AddBookForm";
 
export default (props) => (
  <Popup trigger={<button>Add New Book</button>}>
      {close => (
      <div>
        <AddBookForm addBook={props.addBook}/>
        <a className="close" onClick={close}>
          &times;
        </a>
      </div>
    )}
  </Popup>
);