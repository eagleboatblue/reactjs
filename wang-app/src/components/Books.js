import React from 'react';
import {List, Header, Rating} from 'semantic-ui-react';

export const Books = ({books}) =>{
    return (
        <List>
            {books.map(book => {
                return(
                    <List.Item key={book.title}>
                        <Header>{book.title}</Header>
                        ${book.price}
                    </List.Item>
                )
            })}
        </List>
    )
}