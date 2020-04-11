import React from 'react';
import {List, Header, Rating} from 'semantic-ui-react';

export const Books = ({books}) =>{
    return (
        <List>
            {books.map(book => {
                return(
                    <List.Item key={book.title}>
                        <Header>{book.title}</Header>
                        <Rating maxRating={5}>{book.rating} </Rating>
                        ${book.price}
                    </List.Item>
                )
            })}
        </List>
    )
}