This session was a masterclass in modern data stack troubleshooting. We navigated the complex "middle layer" where Docker networking, database permissions, and metadata orchestration collide. 

---

## 1. The "Parallel Universe" (Local vs. Docker)
The biggest roadblock was the existence of two separate MySQL worlds fighting for the same door (Port 3306). 

* **The Conflict:** You had a **Local MySQL** (Homebrew) and a **Docker MySQL** (OpenMetadata backend). Both wanted to own `localhost:3306`.
* **The Symptom:** In MySQL Workbench, you saw `sakila` and `world` (local), while the OpenMetadata UI was looking for its own system tables (Docker). They were "talking past each other."
* **Lesson Learned:** Always check what is "squatting" on your ports. Using `brew services stop mysql` or checking `lsof -i :3306` is essential when working with containerized databases.

## 2. Airflow Logs: "Who" vs. "What"
We spent time navigating the Airflow UI to find why the crawler wasn't finding your data.

* **Audit Logs:** These only show high-level events (e.g., "Manual run started by admin"). 
* **Task Instance Logs:** These provide the actual "ground truth." This is where we found the critical line: `Processed records: 0`.
* **Lesson Learned:** To debug ingestion, ignore the Audit Log and drill down into the **Logs** tab of the specific Task Instance. Look for schema scan counts and table match patterns.

---

## 3. The "Access Denied" Saga
Even after merging the "universes," the security layers of MySQL provided several final bosses.

* **Docker Networking:** MySQL inside a container sees your Mac as a remote IP (`192.168.65.1`). It doesn't inherently trust `root` unless specifically told to.
* **The Fix:** We used the wildcard grant: `GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'`.
* **Default Schema Trap:** MySQL Workbench tries to "enter" a database upon connection. If that database (like `openmetadata_db`) doesn't exist in the specific instance you're hitting, the connection fails even if the password is correct.
* **Lesson Learned:** Keep the **Default Schema** blank in Workbench until you are certain which instance you are connected to.

## 4. Ingestion Filters & Case Sensitivity
We discovered that the OpenMetadata crawler is precise—and unforgiving.

* **The Hurdle:** Ingestion filters are case-sensitive. If your table is `customers` (lowercase) in MySQL but your filter is `Customers` (uppercase), the crawler will report "Success" but find **0 records**.
* **Lesson Learned:** When in doubt, clear all filters and let the crawler scan the entire schema. Once the data appears, you can use **Excludes** to hide system noise like `information_schema`.

---

## 5. Metadata Governance: Roles vs. Ownership
Finally, we distinguished between "what a person can do" and "who is responsible for the data."

* **Roles (Access Control):** These are global permissions (e.g., Data Steward). If a role like "Data Owner" is missing, you can create a **Custom Role** in the settings.
* **Ownership (Asset Metadata):** This is a field *on the table itself*. You assign an owner to an asset to define accountability, regardless of that user's specific system role.
* **Lesson Learned:** Assigning a **Steward** (technical expert) and an **Owner** (business expert) to the same table is the gold standard for data governance.

