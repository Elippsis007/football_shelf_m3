## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

### HTML
-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/Elippsis007/football_shelf_m3/tree/main/static/images/html_validation)

### CSS
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/Elippsis007/football_shelf_m3/tree/main/static/images/css-validation)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a user, I want the Home page to be simple and easy to understand what the purpose is of the website. When the user enters for the first time they are not exposed to an overload of content.
    
        1. When the user is exploring the website, they will see simple navbar with website name and links to different pages on the website.
        2. The website uses calm, and slightly bright colors.
            
    2. As a user, I want to be able to easily navigate throughout the site to find functions they are looking for.
        
        1. At the top of each page there is a clean navigation bar, each link tells the user which the page they be redirected to.
        2. In mobile phone view there is a drop-down with further links to choose from.
                
    3. As a user, I want the user to be able to explore a library of football books and the ability to contribute to the library upon creating an account.
   
        1. On the Home page the user can Login or Register to the member section. 
        2. On the Home page the user can explore the library of football books and the reviews written by contributers.
        3. The user can also search for football books that contributers have posted.
      
    4. As a user, I want to know what type of functions are available to me.
    
        1. On the Home page the user can explore the library of football books and the reviews written by contributers.
        2. The option to register for an account.
        3. The option after registering for an account to contribute to the library.
        4. To read book reviews by contributors
        5. To leave a personal book review.
        
-   #### Returning User Goals

    1. As a returning user, I want to return to discover old or new football books, that I was unaware of.

        1. The football library has a collapsible list of books titles that can be scrolled through by a simple click of a mouse button.
        2. Here the user can also search for a book title that may have been added into the database by a current member.   
        
    2. As a returning user, I want to add football books that I have either read or simply want to add to the community library.
    
        1. After registration, a user can add a book from their profile page or by navigating to the "Add Book" link.
        2. The user also has the option to remove and edit their book contributions.
        
-   #### Frequent User Goals

    1. As a frequent user, I want to visit the library page to see what newly added football contributions there are.
        
        1. The home page would have some new books.

   ### Further Testing

-  The Website was tested on Google Chrome.
-  The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX using google DevTools.
-  The website has also been tested on <a href="https://responsivedesignchecker.com/">ResponsiveDesignChecker</a> successfully.
-  A large amount of testing was done to ensure that all pages were linking correctly and responsive to all devices.
-  Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

   ### Issues still to fix
-  Defensive programming for when a user wants to delete a book from their library they would be prompeted with a modal to ask if they are certain they want to delete this particular book. Unfortunately after attempts to implement a modal from Materialize this function wouldn't work, when I managed to get the modal to popup and I would hit the delete button, the book I wanted to delete wouldn't but the books below would delete which I certainly wasn't looking to do. I chose not to implement this feature yet until I am able to experiment more with it.
