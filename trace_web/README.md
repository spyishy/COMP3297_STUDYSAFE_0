# StudySafe Trace

StudySafe Trace is the web application aspect of the StudySafe system. It uses the StudySafe Core API to obtain and display the monitored HKU public venues visited by an infected HKU Member. (In the following development, it will be expanded to also obtain and display their close contacts in those venues.)

---

## Usage

StudySafe Trace can be invoked using the following URL:

```
https://studysafe-b-group-e.herokuapp.com/trace/venues/<hku_id>/<date>/
```

StudySafe Trace requires that both `hku_id` and `date` _must_ be provided, and according to their specified formats:

- `hku_id`: A valid HKU ID of an infected HKU Member (unique, max. 10 characters); e.g.: 3030012345
- `date`: Date of diagnosis or onset of symptoms (format: yyyy-mm-dd); e.g.: 2022-04-19

StudySafe Trace will then return a list of Venue Codes of venues visited by the HKU Member within the 2-day infectious period prior to diagnosis/onset.

Below is an example of a valid URL:

```
https://studysafe-b-group-e.herokuapp.com/trace/venues/3030000001/2022-04-17/
```
