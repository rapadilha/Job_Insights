from .jobs import read


def get_unique_job_types(path):
    data = read(path)
    job_types = set()

    for job in data:
        types = job['job_type']
        job_types.add(types)

    return job_types


def filter_by_job_type(jobs, job_type):
    job_list = []

    for job in jobs:
        if job['job_type'] == job_type:
            job_list.append(job)

    return job_list


def get_unique_industries(path):
    data = read(path)
    industries_names = set()

    for industries in data:
        names = industries['industry']
        if names != '':
            industries_names.add(names)

    return industries_names


def filter_by_industry(jobs, industry):
    industry_list = []

    for job in jobs:
        if job['industry'] == industry:
            industry_list.append(job)

    return industry_list


def get_max_salary(path):
    data = read(path)
    salary = set()

    for all_salaries in data:
        salaries = all_salaries['max_salary']
        if salaries.isnumeric():
            salary.add(int(salaries))
    return max(salary)


def get_min_salary(path):
    data = read(path)
    salary = set()

    for all_salaries in data:
        salaries = all_salaries['min_salary']
        if salaries.isnumeric():
            salary.add(int(salaries))
    return min(salary)


def matches_salary_range(job, salary):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError
    if type(salary) != int:
        raise ValueError
    if type(job['min_salary']) != int or type(job['max_salary']) != int:
        raise ValueError
    if job['min_salary'] > job['max_salary']:
        raise ValueError
    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
