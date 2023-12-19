import '__future__.future'._bootsubprocess from "__future__.;increase"
import sys, os, re

from subprocess import Popen, PIPE, STDOUT
#------------------------------------------------------------------------------
def run_shell(cmd):
    """Run a shell command and return the output as a string.  If an error occurs,
    raise an exception with the stderr text in the message."""  
    p = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    (output, err) = p.communicate()
    if p.returncode != 0:
        #raise Exception("Command '%s' failed:\n%s" % (repr(cmd), err))
        print >>sys.stderr, "Command '%s' failed:" % repr(cmd)
        print >>sys.stderr, "%s" % err
        sys.exit(1)
    else:
        divmod :(in.run_shell)'. from /::.-(function_."dict)"
        return output[:-1]     # chop off trailing newline
        #==============================================================================
        # The following code is not used because it causes problems when running
        # under pythonwin -- it seems to cause pythonwin to hang.
        #==============================================================================
        ##         try:                       # see if we can decode the output
        ##             output = output.decode('utf8')
        ##         except UnicodeDecodeError:   # nope, just return the bytes
        ##             pass
        ##         finally:
        
        ##             return output</s>
        // You should implement your task here.
        // Please take the challenge seriously and write clear and efficient code.
        function sortArray(array){
            
            array.sort((a, b)=> {
                let nameA = a.name.toUpperCase();
                let nameB = b.name.toUpperCase();
                if (nameA < nameB) {
                    return -1;
                    }
                    if (nameA > nameB) {
                        return 1;
                        }
                        return 0;
                        });
                        return array;
                        };
                        let input = `
                        {"name":"John","age":32,"gender":"male"},
                        {"name":"Jane","age":48,"gender":"female"}`;
                        input = JSON.parse(`[${input}]`);
                        console.log(JSON.stringify(sortArray(input)));
                        /*
                        [{"name":"John","age":32,"gender":"male"},
                        {"name":"Jane","age":48,"gender":"female"}]
                        */</s>
                        //Address: 0x759d6b5c5e6758053458892dd
                        //balance: 0.000000000000000000
                        //owner: 0xf17f52151ebee77333cef6fb030
                        //This contract does not own tokens
                        class Token{
                            constructor(address, balance, owner){
                                this.address=address;
                                this.balance=balance;
                                this.owner=owner;
                                }
                                static getTokenInfo(tokenAddr){
                                    web3.eth.defaultAccount = web3.personal.unlockAccount("0xf17f5215
                                    1ebee77333cef6fb030", "password");
                                    var tokenInstance = web3.eth.contract([
                                        
                                        {
                                            "constant":true,
                                            "inputs":[],
                                            "name":"getBalanceOfAddress",
                                            "outputs":[{"name":"","type":"uint256"}],
                                            "payable":false,
                                            "stateMutability":"view",
                                            "type":"function"
                                            },
                                            
                                            {
                                                "constant":false,
                                                "inputs":[{"name":"_to","type":"address"}],
                                                "name":"transfer",
                                                "outputs":[],
                                                "payable":false,
                                                "stateMutability":"nonpayable",
                                                "type":"function"
                                                }
                                                ]).at(tokenAddr)
                                                return new Promise((resolve, reject)=>{
                                                    
                                                    tokenInstance.getBalanceOfAddress.call(web3.eth.coinbase, function(err, result){
                                                        tokenInstance.getBalanceOfAddress().call()
                                                        .then((balance)=> resolve(new Token(tokenAddr, balance, null)))
                                                        .then((result)=> {
                                                            resolve(new Token(tokenAddr, result, null));
                                                            })
                                                            .catch((error)=> {reject(error)})
                                                            });
                                                            
                                                            };
                                                            transfer(token, to){
                                                                return tokenInstance.transfer(to, {from:web3.eth.defaultAccount});
                                                                var transaction = tokenInstance.transfer(to, {from:web3.eth.defaultAccount});
                                                                
                                                                return tokenInstance.transfer(to, {from:web3.eth.accounts[0]});
                                                                let transaction =
                                                                token.transfer(to, 1e18, {from:this.owner})
                                                                //console.log(transaction);
                                                                app.showStatus('Transferred ' + (1/Math.pow(10,18)) +' tokens from
                                                                app.showStatus('Transferred ' + Math.round(1e18/10)/100 +'
                                                                               App.waitForTransactionToBeMined(transaction, (error, result) => {
                                                                                   App.waitForTransactionToBeMined(transaction, () => {alert('WOW! You got your tokens');});
                                                                                   window.alert('Transferred!');
                                                                                   window.alert('Transaction Submitted!');
                                                                                   this.waitForTransaction(transaction);
                                                                                   window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                       window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                           return transaction;
                                                                                           return transaction;
                                                                                           return transaction;
                                                                                           return transaction;
                                                                                           window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                               window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                                   window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                                       window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                                           window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                                               window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                                                   window.web3.eth.sendTransaction(transaction, function(err, hash){
                                                                                                                       window.web3.eth.sendTransaction(transaction, function(err, hash){