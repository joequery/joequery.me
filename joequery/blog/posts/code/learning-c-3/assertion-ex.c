#include <stdio.h>
#include <assert.h>  // access to assert() function
int main(){
    int account_balance = 10;
    int product_cost = 20;

    // account_balance isn't allowed to be negative
    assert(account_balance > 0);

    // buy a product...
    account_balance -= product_cost;

    assert(account_balance > 0);
    return 0;
}
