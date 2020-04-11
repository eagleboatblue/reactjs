import React from 'react';
import {List, Header, Rating} from 'semantic-ui-react';
import * as ReactBootStrape from 'react-bootstrap';

export const Books = ({books}) =>{
    return (
        <List>
            {books.map(book => {
                return(
                    <ReactBootStrape.Table border="1">
                    <List.Item key={book.title}>
                    <tr>
                        <td>{book.title}</td>
                        <td>${book.price}</td>
                    </tr>
                    </List.Item>
                    </ReactBootStrape.Table>
                )
            })}
        </List>
    )
}