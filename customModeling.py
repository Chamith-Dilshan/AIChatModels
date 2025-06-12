import subprocess

model_name = "violet"
modelfile_path = "./Modelfile"  # No extension!

try:
    result = subprocess.run(
        ["ollama", "create", model_name, "-f", modelfile_path],
        capture_output=True,
        text=True,
        check=True
    )
    print(f"✅ Model '{model_name}' created successfully!")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"❌ Failed to create model '{model_name}':\n{e.stderr}")
