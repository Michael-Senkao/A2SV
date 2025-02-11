# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class Token:
    def __init__(self, id = "", expire = 0):
        self.id = id
        self.expire = expire
        self.next = None
        self.prev = None

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.ids = {}
        self.active_tokens = 0

        self.head, self.tail = Token(0), Token(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def add(self, token: Token):
        token.next = self.tail
        token.prev = self.tail.prev
        token.prev.next = token
        token.next.prev = token

        self.ids[token.id] = token
        self.active_tokens += 1
    
    def remove(self, token: Token):
        token.prev.next = token.next
        token.next.prev = token.prev

        del self.ids[token.id]
        self.active_tokens -= 1
       

    def generate(self, tokenId: str, currentTime: int) -> None:
        token = Token(tokenId, currentTime + self.time_to_live) # Create new token
        self.add(token) # Add the new token
       

    def renew(self, tokenId: str, currentTime: int) -> None:
        token = self.ids.get(tokenId, None) # Get address of current token
        
        if token is None:
            return # Id does not exist

        self.remove(token) # Remove current token from token list

        # Check if token is already expired
        if currentTime >= token.expire:
            return 

        token.expire = currentTime + self.time_to_live # Update expiry time
        self.add(token) # Add token back to token list
       

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # Remove expired tokens from token list
        while self.active_tokens and currentTime >= self.head.next.expire:
            self.remove(self.head.next)
        
        return self.active_tokens # return active tokens


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)