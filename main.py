try:
    from googlesearch import search
    import sys
except:
    print('python3 -m pip install googlesearch-python')
    exit()

def main():
    for dork in sys.stdin:
        dork = dork.strip('\n')
        results = list(search(dork, num_results=1000))
        for result in results:
            print(result)
    
main()