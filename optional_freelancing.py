def job_fits(job, deadline):
    fits = job["deadline"] >= deadline
    print(f"{job} fits {deadline}={fits}")
    return fits
        
def best_option(jobs, deadline):
    best = None
    for job in jobs:
        if job_fits(job, deadline) and (best == None or job["payment"] > best["payment"]):
            best = job
    return best
    
def optimalFreelancing(jobs):
    pay = 0
    for day in range(7, 0, -1):
        best = best_option(jobs, day)
        print(best)
        if best != None:
            pay += best["payment"]
            jobs.remove(best)
    return pay

