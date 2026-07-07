$sourceDir = "word-drafts"
$targetDir = "content/1-Worklog" # Bạn có thể thay đổi đường dẫn này nếu muốn lưu vào folder khác

# Kiểm tra thư mục đích, nếu chưa có thì tạo
if (-not (Test-Path -Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir | Out-Null
}

# Kiểm tra Pandoc đã nhận chưa
if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Host "Lỗi: Máy tính chưa nhận diện được Pandoc." -ForegroundColor Red
    Write-Host "Vui lòng tắt hoàn toàn VS Code / Terminal và mở lại để hệ thống nhận diện Pandoc." -ForegroundColor Yellow
    exit
}

# Lấy danh sách các file .docx trong thư mục word-drafts
$files = Get-ChildItem -Path $sourceDir -Filter *.docx

if ($files.Count -eq 0) {
    Write-Host "Không tìm thấy file .docx nào trong thư mục '$sourceDir'." -ForegroundColor Yellow
    exit
}

foreach ($file in $files) {
    $baseName = $file.BaseName
    
    # Định dạng tên file output: Chữ thường, thay khoảng trắng bằng dấu gạch ngang
    $mdFileName = $baseName.ToLower().Replace(" ", "-") + ".md"
    $mdFilePath = Join-Path -Path $targetDir -ChildPath $mdFileName
    
    Write-Host "Đang chuyển đổi '$($file.Name)' -> '$mdFileName'..." -ForegroundColor Green
    
    # Chạy Pandoc để chuyển đổi sang Markdown
    pandoc $file.FullName -t markdown --wrap=none -o $mdFilePath
    
    # Tự động thêm Front Matter cho file Hugo
    $currentDate = (Get-Date).ToString("yyyy-MM-dd")
    
    $frontMatter = @"
---
title : "$baseName"
date : $currentDate
weight : 1
chapter : false
---

"@

    # Đọc nội dung file Markdown vừa tạo và chèn Front Matter lên đầu
    $content = Get-Content $mdFilePath -Raw
    $newContent = $frontMatter + $content
    Set-Content -Path $mdFilePath -Value $newContent -Encoding UTF8
}

Write-Host "Hoàn tất! Các file đã được lưu trong thư mục $targetDir." -ForegroundColor Cyan
