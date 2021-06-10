## Instructions to test the contract
* Open the [Remix IDE](https://remix.ethereum.org/) and create a new *.*sol* file. 

* Copy and Paste the code present inside **loanContract.sol** to Remix IDE and compile the code. 
 
 #### Dry run for testing all the functions implemented inside the loan contract which inherits Metacoin smartcontract
 * On the left sidebar in Remix IDE, choose the option to Deploy the Smart Contract. 
 * Choose Loan-contracts/assignment2.sol in contracts option
 * Choose one account of your choice and deploy the contract (this will act as the owner account)
 * You can verify the initial balance of the Owner by calling **getOwnerBalance** function to be 100000
 * Now choose some other account , for now we will refer it as **creditor**.
 
 #### Testing getCompoundInterest(...)
 * Pass your desired arguements from the Remix sidebar as (principal , rate (as an upto two digit decimal) , time) 
 * For ex .. on 100,10,2 output comes out to be 121 
 * Compound Interest is calculated by repeatedly incrementing principal by (rate%) at the end of every year using a for loop.
 * **Note** this function is **pure** as it does not access any state variable.
 
 ### Lets begin with the example 
 **reqLoan**
 * Now from the creditor account call **reqLoan** with (principal , rate of interest(as an upto two digit decimal) , time elapsed since the provision of loan) . This should add a key value pair in balances mapping with address of the creditor as key and getCompoundInterest(parameters) as value( which we will check next). For our example consider the arguements to **reqLoan** be (100,10,2) which should add 121 as amount.
 * **Note** reqLoan is niether view nor pure type as it modifies the state of the contract to add/modify a key value pair in the balances mapping.
 
**viewDues**
 * Copy the address of the creditor account and paste it in **viewDues** and call the function , wait what it doesnt work , reason being it can only be accessed by owner because of **isOwner** modifier , so first switch the account back to the owner which was used to deploy the contract and again call the **viewDues** function , 121 shows up hence everything is working fine till now.
* **note** ViewDues is a view function as it just accesses the state values but does not modify anything 

**settleDues**
* Now lets try to settle the dues of creditor account .To do so call **settleDues** function from owner account with Creditor address as arguement.
* Then call **viewDues** function with the creditor address , which returns zero as dues are already settled .
* Finally Lets check the balance of the owner after settling dues by calling **getOwnerBalance()** , and it comes out to be  99879 units , indeed it got reduced by 121 units.
* **note** - If you call **settleDues** from some other account other than the owner it will not work because of the modifier.
