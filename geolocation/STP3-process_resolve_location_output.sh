#!/usr/bin/awk -f
BEGIN{
  FS=" : ";
  failed_count=0;
  success_count=0;
}
{
  if($1=="SUCCESS"){
    success_count++;
    size=split($3,temp,",");
    print $2 " : " temp[size]
  } else {
    failed_count++
  }
}
END{
  print "LOCATED: " success_count " and FAILED: " failed_count
}
