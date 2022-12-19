def get_output_string():
  place, animal, job, badsmell = input("Enter a place, animal, job, and bad smell: ").split()
  return f"We went to {place} to see a {animal} but a {job}er said go away. I said why? They said you smell like {badsmell}"

output_string = get_output_string()
print(output_string)
