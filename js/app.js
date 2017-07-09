import Hello from './Hello';
import ShoppingList from './List';
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(<Hello/>, document.getElementById('reactEntry'));
ReactDOM.render(<ShoppingList/>, document.getElementById('shopping-list'));
