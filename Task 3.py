#Enock Kibet
#CIT-227-068/2024
% --- Genders ---
male(john).      % Grandfather
male(david).     % Uncle
male(tom).       % Parent
male(paul).      % Cousin 1
male(mark).      % Cousin 2

female(mary).    % Grandmother
female(ann).     % Parent
female(sarah).   % Aunt
female(emily).   % Cousin 3

% --- Parent Relations ---
% Grandparents to Parents
parent(john, david).
parent(john, sarah).
parent(mary, david).
parent(mary, sarah).

% David and Ann's kids
parent(david, paul).
parent(david, emily).
parent(ann, paul).
parent(ann, emily).

% Sarah and Tom's kids
parent(sarah, mark).
parent(tom, mark).

% --- Rules ---

% Siblings share a parent and are not the same person
sibling(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y), 
    X \= Y.

% Grandparents
grandparent(GP, GC) :- 
    parent(GP, P), 
    parent(P, GC).

grandfather(GF, GC) :- grandparent(GF, GC), male(GF).
grandmother(GM, GC) :- grandparent(GM, GC), female(GM).

% Grandchildren
grandchild(GC, GP) :- grandparent(GP, GC).

% Uncles and Aunts (siblings of a parent)
uncle(U, N) :- 
    parent(P, N), 
    sibling(U, P), 
    male(U).

aunt(A, N) :- 
    parent(P, N), 
    sibling(A, P), 
    female(A).

% Cousins (parents are siblings)
cousin(X, Y) :- 
    parent(P1, X), 
    parent(P2, Y), 
    sibling(P1, P2),
    X \= Y.
