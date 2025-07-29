# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingre in ingredients[i]:
                graph[ingre].append(recipe)
                indegree[recipe] += 1

        q = deque()
        for recipe, ingre in graph.items():
            if indegree[recipe] == 0 and recipe in supplies:
                q.append(recipe)

        canMake = []
        while q:
            ingre = q.popleft()
            for recipe in graph[ingre]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    q.append(recipe)
                    canMake.append(recipe)


        return canMake