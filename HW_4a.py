import requests

def request(user):

    #Receive response from api
    repoList = requests.get('https://api.github.com/users/' +user+ '/repos')
    #convert to json format
    resultRepo = repoList.json()

    #initialize return array
    answer = []

    #verify that a user was found (when a user is not found the response is of length 2)
    if isinstance(resultRepo, dict):
        return "Unable to find user with the inputted ID."
    else:
        #loop through each repo and obtain their respective number of commits
        for repo in resultRepo:
            commitList = requests.get('https://api.github.com/repos/'+user+'/'+repo["name"]+'/commits')
            resultCommit = commitList.json()

            #ensure the number of commits is not 0 since it would return a dictionary if there were no commits found
            if isinstance(resultCommit, dict):
                answer.append('Repo: ' +repo["name"] + " Number of commits: " + str(0))
            else:       
                commitLength = str(len(resultCommit))
                #add repo and its respective number of commits to return array
                answer.append('Repo: ' +repo["name"] + " Number of commits: " + commitLength)

        #ensure that repos were found
        if answer == []:
            return "This user has no current repos."
        else:
            return answer
        
if __name__ == "__main__":
    user = input("Enter a user ID: ")
    trimUser = user.strip()
    result = request(trimUser)
    if isinstance(result, str):
        print(result)
    else:
        #print(result)
        for x in result:
            print(x)

    
    
