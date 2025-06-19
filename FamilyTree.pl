father(john, mary).
father(john, tom).
father(john, sarah).
mother(susan, mary).
mother(susan, tom).
mother(susan, sarah).

father(david, alice).
father(david, bob).
mother(mary, alice).
mother(mary, bob).

father(tom, charlie).
father(tom, diana).
mother(linda, charlie).
mother(linda, diana).

father(michael, eve).
father(michael, frank).
mother(sarah, eve).
mother(sarah, frank).

male(john).
male(tom).
male(david).
male(bob).
male(charlie).
male(michael).
male(frank).

female(susan).
female(mary).
female(sarah).
female(linda).
female(alice).
female(diana).
female(eve).

spouse(john, susan).
spouse(susan, john).
spouse(mary, david).
spouse(david, mary).
spouse(tom, linda).
spouse(linda, tom).
spouse(sarah, michael).
spouse(michael, sarah).


parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).


grandfather(X, Z) :- father(X, Y), parent(Y, Z).
grandmother(X, Z) :- mother(X, Y), parent(Y, Z).

grandparent(X, Z) :- grandfather(X, Z).
grandparent(X, Z) :- grandmother(X, Z).

sibling(X, Y) :- father(F, X), father(F, Y), mother(M, X), mother(M, Y), X \= Y.
halfSiblingfather(X, Y) :- father(F, X), father(F, Y), mother(M1, X), mother(M2, Y), M1 \= M2, X \= Y.
halfSiblingMother(X, Y) :- mother(M, X), mother(M, Y), father(F1, X), father(F2, Y), F1 \= F2, X \= Y.

halfSibling(X, Y) :- half_sibling_father(X, Y).
halfSibling(X, Y) :- half_sibling_mother(X, Y).

brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).

uncle(X, Y) :- male(X), parent(Z, Y), sibling(X, Z).
maternalUncle(X, Y) :- male(X), mother(M, Y), sibling(X, M).
paternalUncle(X, Y) :- male(X), father(F, Y), sibling(X, F).

aunt(X, Y) :- female(X), parent(Z, Y), sibling(X, Z).
auntie(X, Y) :- aunt(X, Y).
maternalAunt(X, Y) :- female(X), mother(M, Y), sibling(X, M).
paternalAunt(X, Y) :- female(X), father(F, Y), sibling(X, F).

nephew(X, Y) :- male(X), parent(Z, X), sibling(Z, Y).
niece(X, Y) :- female(X), parent(Z, X), sibling(Z, Y).

son(X, Y) :- male(X), parent(Y, X).
daughter(X, Y) :- female(X), parent(Y, X).

grandchild(X, Y) :- grandparent(Y, X).
grandson(X, Y) :- male(X), grandchild(X, Y).
granddaughter(X, Y) :- female(X), grandchild(X, Y).
cousin(X, Y) :- parent(Z, X), parent(W, Y), sibling(Z, W), X \= Y.


fatherInlaw(X, Y) :- father(X, Z), spouse(Y, Z).
motherInlaw(X, Y) :- mother(X, Z), spouse(Y, Z).

sonInlaw(X, Y) :- male(X), spouse(X, Z), parent(Y, Z).
daughterInlaw(X, Y) :- female(X), spouse(X, Z), parent(Y, Z).

brotherInlaw(X, Y) :- male(X), spouse(Y, Z), sibling(X, Z).
sisterInlaw(X, Y) :- female(X), spouse(Y, Z), sibling(X, Z).